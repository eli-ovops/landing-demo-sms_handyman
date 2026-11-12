import {fileURLToPath} from 'node:url';
import {chromium} from '/Users/USER/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
const browser=await chromium.launch({channel:'chrome',headless:true});
try {
for(const [name,width,height] of [['desktop',1440,900],['mobile',390,844]]) {
const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
await page.goto('http://127.0.0.1:8768/',{waitUntil:'load',timeout:20000});
await page.evaluate(()=>document.fonts.ready);
await page.evaluate(async()=>{for(const img of document.images){img.loading='eager';} await Promise.all([...document.images].map(img=>img.decode()));});
await page.screenshot({path:fileURLToPath(new URL(`email-${name}.png`,import.meta.url)),fullPage:true,timeout:15000});
console.log(name,await page.title());
await page.close();
}
} finally {await browser.close();}
