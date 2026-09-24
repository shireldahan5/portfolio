// main.js, Shirel Dahan portfolio
//
// The site works without JavaScript. This file adds one extra:
// a "Copy address" button on the contact page.

const copyButton = document.querySelector('[data-copy]');
const copyStatus = document.querySelector('.copy-status');

// Only show the button if the browser lets us write to the clipboard
if (copyButton && navigator.clipboard) {
  copyButton.hidden = false;

  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(copyButton.dataset.copy);
      copyStatus.textContent = 'Copied to your clipboard.';
    } catch {
      copyStatus.textContent = 'Could not copy. The address is above.';
    }
  });
}
