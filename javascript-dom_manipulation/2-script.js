const header = document.querySelector('header');
const button = document.querySelector('#red_header')
button.addEventListener('click', () => {
	header.classList.add('red');
});