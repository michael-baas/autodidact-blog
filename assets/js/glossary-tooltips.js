(function() {
  async function loadGlossary() {
    const res = await fetch('{{ "/_data/glossary.json" | relative_url }}');
    return res.ok ? res.json() : {};
  }
  function attach(glossary) {
    document.querySelectorAll('.term[data-term]').forEach(el => {
      const key = (el.getAttribute('data-term') || '').toLowerCase();
      const def = glossary[key];
      if (!def) return;
      el.setAttribute('title', def); // native hover tooltip
      // Optional: upgrade to a styled tooltip later
    });
  }
  document.addEventListener('DOMContentLoaded', () => {
    loadGlossary().then(attach).catch(() => {});
  });
})();
