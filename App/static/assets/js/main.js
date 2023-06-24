const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close')


if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}

if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

const navLink = document.querySelectorAll('.nav__link')


function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

let swiper = new Swiper(".discover__container", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    loop: true,
    spaceBetween: 32,
    coverflowEffect: {
        rotate: 0,
    },
})

function scrollUp() {
    const scrollUp = document.getElementById('scroll-up');
    if (this.scrollY >= 200) scrollUp.classList.add('show-scroll');
    else scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

const sections = document.querySelectorAll('section[id]')


function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        } else {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

const sr = ScrollReveal({
    distance: '60px',
    duration: 1000,
    reset: true,
})


sr.reveal(`.home__data, .home__social-link, .home__info,
           .discover__container,
           .section__title,
           .experience__data, .experience__overlay,
           .place__card,.form-group,
           .article__title,.video__title,
           .h__subtitle,
           .sponsor__content,
           .footer__data, .footer__rights`, {
    origin: 'top',
    interval: 100,
})

sr.reveal(`.about__data,.sl-fb,.sl-ig,.sl-tw,.sl-wp,.sl-yt,
           .hl-fb,.hl-ig,.hl-tw,.hl-wp,.hl-yt, 
            .video__description,
            .article__description,
            .article__para,.rit,
            .h__star,.w3-card-4,
            .subscribe__description,.hotel__data`, {
    origin: 'left',
    interval: 100,
})

sr.reveal(`.about__img-overlay,
            .article__star,.video__star,
            .hotel__card,
            .h__title,.page-btn,
           .subscribe__form`, {
    origin: 'right',
    interval: 100,
})

sr.reveal(`.al-em,.al-fb,.al-ig,.al-pn,.al-tw,.al-wp`, {
    origin: 'right',
    interval: 600,
})

sr.reveal(`.place__title,.place__subtitle,.place__price`, {
    origin: 'left',
    interval: 200,
})

sr.reveal(`.ri-first-aid-kit-fill,.ri-goblet-fill,
.ri-restaurant-fill,.ri-roadster-fill,.ri-wifi-fill`, {
    origin: 'right',
    interval: 300,
})

const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'ri-sun-line'
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'ri-moon-line' : 'ri-sun-line'


if (selectedTheme) {
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
    themeButton.classList[selectedIcon === 'ri-moon-line' ? 'add' : 'remove'](iconTheme)
}

themeButton.addEventListener('click', () => {
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000);
}

function myFunction() {
    var password = document.getElementById("loginpassword");
    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}

function myFunction2() {
    var password2 = document.getElementById("pass1");
    if (password2.type === "password") {
        password2.type = "text";
    } else {
        password2.type = "password";
    }
}

function myFunction3() {
    var password3 = document.getElementById("pass2");
    if (password3.type === "password") {
        password3.type = "text";
    } else {
        password3.type = "password";
    }
}