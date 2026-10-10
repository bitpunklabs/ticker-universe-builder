#!/usr/bin/env node
/* Optional documentation tool. Requires Playwright and an installed Chrome browser. */
const { chromium } = require('playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

const root = path.resolve(__dirname, '..');

async function main() {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const page = await browser.newPage({
    viewport: { width: 880, height: 1000 },
    deviceScaleFactor: 1,
    colorScheme: 'dark',
  });
  const receipts = [];
  try {
    const folders = (await fs.readdir(__dirname, { withFileTypes: true }))
      .filter(entry => entry.isDirectory() && /^(cn|us|crypto|hk|jp|kr|uk)-/.test(entry.name))
      .map(entry => entry.name).sort();
    for (const folder of folders) {
      const output = path.join(__dirname, folder, 'output');
      const files = (await fs.readdir(output)).filter(file => file.endsWith('.html')).sort();
      const preview = path.join(__dirname, folder, 'preview');
      await fs.mkdir(preview, { recursive: true });
      for (const file of files) {
        const input = path.join(output, file);
        const stem = file.slice(0, -5);
        await page.setViewportSize({ width: 880, height: 1000 });
        await page.goto(pathToFileURL(input).href, { waitUntil: 'load' });
        await page.evaluate(() => document.fonts.ready);
        const stats = await page.evaluate(() => ({
          title: document.title,
          height: document.documentElement.scrollHeight,
          entries: document.querySelectorAll('.entry').length,
          horizontalOverflow: document.documentElement.scrollWidth > innerWidth,
        }));
        if (stats.horizontalOverflow) throw new Error(`${file}: horizontal overflow`);
        const universe = JSON.parse(await fs.readFile(input.replace(/\.[^.]+\.html$/, '.json'), 'utf8'));
        const expected = universe.members.length + universe.coverage_plan.references.length;
        if (stats.entries !== expected) throw new Error(`${file}: ${stats.entries} rows, expected ${expected}`);
        await page.screenshot({ path: path.join(preview, `${stem}.jpg`), type: 'jpeg', quality: 88 });
        await page.screenshot({ path: path.join(preview, `${stem}.full.jpg`), type: 'jpeg', quality: 75, fullPage: true });
        if (folder === 'us-medium' && file.endsWith('.en.html')) {
          const media = path.join(root, 'docs', 'media');
          await fs.mkdir(media, { recursive: true });
          await fs.copyFile(path.join(preview, `${stem}.jpg`), path.join(media, 'us-medium-preview.jpg'));
          await page.setViewportSize({ width: 390, height: 1000 });
          const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
          if (overflow) throw new Error(`${file}: mobile horizontal overflow`);
          await page.screenshot({ path: path.join(media, 'us-medium-preview-mobile.jpg'), type: 'jpeg', quality: 88 });
        }
        receipts.push({ report: path.relative(root, input), ...stats, expected });
        console.log(`${folder}/${file}: ${stats.entries} rows; ${stats.height}px; preview + full image`);
      }
    }
  } finally {
    await browser.close();
  }
  const receiptDir = path.join(root, 'temp', 'report-previews');
  await fs.mkdir(receiptDir, { recursive: true });
  await fs.writeFile(path.join(receiptDir, 'capture-receipt.json'), JSON.stringify({
    capturedAt: new Date().toISOString(),
    browser: 'Playwright Chromium, installed Chrome channel',
    viewport: { width: 880, height: 1000 },
    reports: receipts,
  }, null, 2) + '\n');
}

main().catch(error => { console.error(error); process.exitCode = 1; });
