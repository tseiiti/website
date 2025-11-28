
function qs(arg) { return document.querySelector(arg) }
function qsa(arg) { return document.querySelectorAll(arg) }
function on(arg, eve, func) {
  qsa(arg).forEach(e => {
    e.addEventListener(eve, function() { func(e) })
  });
}

// controla de temas
function setTheme(theme) {
  qs('html').dataset.bsTheme = theme;
  let i = qs('.i-theme');
  if (!i) return;
  if (theme == 'dark') {
    i.classList.remove('fa-sun');
    i.classList.add('fa-moon');
  } else {
    i.classList.remove('fa-moon');
    i.classList.add('fa-sun');
  }
  localStorage.setItem('theme', theme);
}

window.addEventListener('DOMContentLoaded', event => {
  if (localStorage.theme) setTheme(localStorage.theme);

  // flechas collapse
  on('div.collapse', 'show.bs.collapse', function (e) {
    let i = qs(`[href="#${e.id}"]`).querySelector('.i-theme-arrow');
    i.classList.remove('fa-chevron-right');
    i.classList.add('fa-chevron-down');
  });
  on('div.collapse', 'hidden.bs.collapse', function (e) {
    let i = qs(`[href="#${e.id}"]`).querySelector('.i-theme-arrow');
    i.classList.remove('fa-chevron-down');
    i.classList.add('fa-chevron-right');
  });
});