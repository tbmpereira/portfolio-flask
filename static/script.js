/* Abre e fecha menu lateral em modo mobile */

const menuMobile = document.querySelector('.menu-mobile');

const body = document.querySelector('body');

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");
    body.classList.toggle('menu-nav-active');
});

/* Fecha menu lateral ao clicar em um link */

const navItem = document.querySelectorAll('.nav-item');

navItem.forEach(item => {
    item.addEventListener('click', () => {
        if(body.classList.contains('menu-nav-active')){
            menuMobile.classList.replace("bi-x", "bi-list");
            body.classList.remove('menu-nav-active');
        }
    });
})