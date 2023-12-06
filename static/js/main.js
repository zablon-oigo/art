
// let slides = document.getElementsByClassName("image");
// let slideIndex = 0;
// showSlide();

// function showSlide() {
//     for (let i = 0; i < slides.length; i++) {
//         slides[i].style.display = 'none';
//     }

//     slideIndex++;
//     if (slideIndex > slides.length) {
//         slideIndex = 1;
//     }

//     slides[slideIndex - 1].style.display = 'block';
//     setTimeout(showSlide, 3000);
// }


const mycards=document.getElementsByClassName("card")
let cardIndex=0
showCard();
function showCard(){
  

    for (let i = 0; i < mycards.length; i++) {
        mycards[i].classList.add('hidden');
        
    }
    cardIndex++;
    if (cardIndex > mycards.length) {
        cardIndex = 1;
    }
    mycards[cardIndex - 1].classList.remove('hidden');
    setTimeout(showCard, 3000);
}