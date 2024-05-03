/* Project specific Javascript goes here. */
const nav = document.querySelector('.nav');
const burger = document.querySelector('.burger')

console.log(nav);
console.log(burger);


burger.addEventListener('click', (e)=>{
    nav.classList.toggle('nav--active');
    burger.classList.toggle('burger--active');
    e.preventDefault();
});