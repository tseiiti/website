function qs(arg) { return document.querySelector(arg) }
function qsa(arg) { return document.querySelectorAll(arg) }

// controla de temas
function setTheme(theme) {
  qs('html').dataset.bsTheme = theme;
  if (theme == 'dark') {
    let i = qs('.i-theme');
    i.classList.remove('fa-sun');
    i.classList.add('fa-moon');
  } else {
    let i = qs('.i-theme');
    i.classList.remove('fa-moon');
    i.classList.add('fa-sun');
  }
  localStorage.setItem('theme', theme);
}

window.addEventListener('DOMContentLoaded', event => {
  if (localStorage.theme) setTheme(localStorage.theme);

  // flechas collapse
  qs('#collapse-theme').addEventListener('show.bs.collapse', function () {
    let i = qs('.i-theme-arrow');
    i.classList.remove('fa-chevron-right');
    i.classList.add('fa-chevron-down');
  });
  
  qs('#collapse-theme').addEventListener('hidden.bs.collapse', function () {
    let i = qs('.i-theme-arrow');
    i.classList.remove('fa-chevron-down');
    i.classList.add('fa-chevron-right');
  });
});
