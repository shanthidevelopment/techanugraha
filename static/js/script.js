let menubtn=document.querySelector("#menu-btn")
let menulist=document.querySelector("#menu-list")

menubtn.addEventListener("click",()=>{
    menulist.classList.toggle("show")
})

let menus=document.querySelectorAll("#menus")

menus.forEach(
    (e)=>{
        e.addEventListener("click",()=>{
            menulist.classList.remove("show")
        })
    }
)


