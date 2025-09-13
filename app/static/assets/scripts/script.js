const mainElement = document.getElementById('main');
const leftSidebarElement = document.getElementById('left-sidebar');
const rightSidebarElement = document.getElementById('right-sidebar');

const buttons = document.getElementsByClassName('mobile-nav-button');

for (let i = 0; i < buttons.length; i++) {

    buttons[i].addEventListener('click', function() {

        mainElement.classList.add('hidden');
        leftSidebarElement.classList.add('hidden');
        rightSidebarElement.classList.add('hidden');

        const targetId = this.getAttribute('data-target');
        const targetElement = document.getElementById(targetId);
        targetElement.classList.remove('hidden');

    });

}