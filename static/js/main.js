


const testimonials = document.getElementsByClassName("testimonials");
let cardIndex = 0;
showCard();

function showCard() {
    for (let i = 0; i < testimonials.length; i++) {
        testimonials[i].classList.add('hidden');
    }

    cardIndex++;
    if (cardIndex > testimonials.length) {
        cardIndex = 1;
    }

    testimonials[cardIndex - 1].classList.remove('hidden');
    setTimeout(showCard, 3000);
}
