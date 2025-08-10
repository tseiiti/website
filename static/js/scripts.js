window.addEventListener('DOMContentLoaded', event => {
  const mobileScreen = window.matchMedia('(max-width: 990px)');

  document.querySelectorAll('.dashboard-nav-dropdown-toggle')
  .forEach(element => {
    element.addEventListener('click', function () {
      this.closest('.dashboard-nav-dropdown')
        .classList.toggle('show');
    });
  });

  document.querySelectorAll('.menu-toggle')
  .forEach(element => {
    element.addEventListener('click', function () {
      if (mobileScreen.matches) {
        document.querySelectorAll('.dashboard-nav').forEach(element => {
          element.classList.toggle('mobile-show');
        });
      } else {
        document.querySelectorAll('.dashboard').forEach(element => {
          element.classList.toggle('dashboard-compact');
        });
      }
    });
  });

});