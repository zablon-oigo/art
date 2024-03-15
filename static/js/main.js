innitApp=()=>{
    const menuBtn =document.querySelector('#menuBtn')
    const menu =document.querySelector('#menu')
   
       const toggleMenu=()=>{
           menu.classList.toggle('hidden')
           menu.classList.toggle('flex')
   
   
       }
       menuBtn.addEventListener('click',toggleMenu)
   
   }
   document.addEventListener('DOMContentLoaded',innitApp)

