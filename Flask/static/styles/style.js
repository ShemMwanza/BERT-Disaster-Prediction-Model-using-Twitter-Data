const navbarmenu = document.getElementById('navbar-menu');
const menu = document.getElementById('menu-btn');
const menu1 = document.getElementById('menu-btn1');

function openMenu() {
    navbarmenu.classList.remove("hidden");
    menu1.classList.remove("hidden");
    menu.classList.add("hidden");
}
function closeMenu() {
    navbarmenu.classList.add("hidden");
    menu1.classList.add("hidden");
    menu.classList.remove("hidden");
}

