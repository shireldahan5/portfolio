// main.js, Shirel Dahan portfolio
//
// The site works without JavaScript. This file adds:
//   1. Reveal on scroll: adds .is-in so CSS can animate things in
//   2. A header that hides while you scroll down and comes back up
//   3. Tabs for the screen viewer on the case study page
//   4. The "Copy address" button on the contact page


// ── 1. Reveal on scroll ─────────────────────────────────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-in');
      revealObserver.unobserve(entry.target); // only animate once
    }
  });
}, { rootMargin: '0px 0px -8% 0px' });

document.querySelectorAll('[data-reveal]').forEach((el) => revealObserver.observe(el));


// ── 2. Header ───────────────────────────────────────────────────
// requestAnimationFrame means we check at most once per frame,
// however many scroll events fire.
const header = document.querySelector('.site-header');
let lastY = window.scrollY;
let ticking = false;

function updateHeader() {
  const y = window.scrollY;
  header.classList.toggle('is-scrolled', y > 10);
  // Hide only after the first screenful, and only when scrolling down
  header.classList.toggle('is-hidden', y > lastY && y > window.innerHeight * 0.6);
  lastY = y;
  ticking = false;
}

window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(updateHeader);
    ticking = true;
  }
}, { passive: true });

// Keyboard users tabbing into the header should always see it
header.addEventListener('focusin', () => header.classList.remove('is-hidden'));


// ── 3. Screen viewer tabs ───────────────────────────────────────
// Follows the WAI-ARIA tabs pattern: click or use the arrow keys,
// and only the selected tab is in the Tab order.
const viewer = document.querySelector('[data-viewer]');

if (viewer) {
  const tablist = viewer.querySelector('[role="tablist"]');
  const tabs = [...viewer.querySelectorAll('[role="tab"]')];

  tablist.hidden = false;
  viewer.classList.add('has-tabs');

  function select(tab) {
    tabs.forEach((t) => {
      const selected = t === tab;
      t.setAttribute('aria-selected', String(selected));
      t.tabIndex = selected ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls'))
        .classList.toggle('is-active', selected);
    });
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => select(tab));

    tab.addEventListener('keydown', (event) => {
      let next = null;
      if (event.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      if (event.key === 'ArrowLeft')  next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (event.key === 'Home')       next = tabs[0];
      if (event.key === 'End')        next = tabs[tabs.length - 1];
      if (next) {
        event.preventDefault();
        select(next);
        next.focus();
      }
    });
  });
}


// ── 4. Copy email address ───────────────────────────────────────
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
