// let paragraph = document.querySelectorAll(".X")
// console.log(paragraph[0].innerHTML)
// console.log(paragraph[1])



// const myId = document.getElementById("X")
// console.log(myId)


// let myClass = document.getElementsByClassName("X")
// console.log(myClass[0].innerHTML)
// console.log(myClass[1].outerHTML)



// const h1 = document.querySelector("h1")
// console.log(h1)

// const idP = document.querySelector("#test2")
// console.log(idP)

// let h2 = document.querySelectorAll("h2")

// h2.forEach(element => {
//     console.log(element)
// });


// let classP = document.querySelectorAll(".test1")

// classP.forEach(i => {
//     console.log(i)
// })

// let xclassP = document.getElementsByClassName("test1")

// classP.forEach(element => {
//     console.log(element)
// });

// let xidP = document.getElementById("test2")
// console.log(xidP)


// let heading = document.querySelector("h1")
// console.log(heading.textContent)
// // console.log(heading.innerHTML)

// heading.textContent = "New"


// let list = document.querySelectorAll("p")

// list.forEach(element => {
//     if(element.textContent.toLowerCase().includes("nakrmit")){
//         element.remove()
//     }
// });



// const newP = document.createElement("p")
// newP.textContent = "Novy text"

// document.querySelector("header").appendChild(newP)

// const newDiv = document.createElement("div")
// document.querySelector("header").appendChild(newDiv)

// const secPar = document.createElement("p")
// secPar.textContent = "Test div"
// newDiv.appendChild(secPar)

// const newSPan = document.createElement("span")
// newSPan.textContent = "SPPPPPPPPPPPAN"
// secPar.prepend(newSPan)



// let ToDo = [{
//     text: "Vynest kos",
//     finished: false
// },{
//     text: "Nakoupit",
//     finished: false
// },{
//     text: "Uklidit",
//     finished: false
// },{
//     text: "Pes",
//     finished: true
// },{
//     text: "Kocka",
//     finished: false
// }]

// let x = 0
// ToDo.forEach(element => {
//     if(element.finished == 0){
//         x++
//         const newTTD = document.createElement("p")
//         newTTD.textContent = element.text
//         document.querySelector("main").appendChild(newTTD)
//     }
// });
// const num = document.createElement("p")
// num.textContent = `Počet úkolů k dokončení: ${x}`
// document.querySelector("main").appendChild(num)


// document.querySelector("a").addEventListener("click", function(event){
//     console.log(event.target.textContent = "jojo")
// })



// document.querySelector("h1").addEventListener("click",function(event) {
//     event.target.textContent = "Klikni na nadpis nize"
// })

// document.querySelector("h2").addEventListener("click",function(event) {
//     event.target.textContent = "Klikni na nadpis nize"
// })
// document.querySelector("h3").addEventListener("click",function(event) {
//     event.target.textContent = "Klikni na nadpis nize"
// })


// let input = document.querySelector("#input_text")
// input.addEventListener("input", function(event){
//     console.log(event.target.value)
// })


// let criminals = [{
//     firstName: "Martin",
//     secondName: "Zelený",
//     birth: 1985,
//     licencePlate: "85C3322",
//     address: "U sloupů 16",
//     city: "České Budějovice"
// }, {
//     firstName: "Jana",
//     secondName: "Růžová",
//     birth: 1996,
//     licencePlate: "93K3922",
//     address: "Malská 29",
//     city: "České Budějovice"
// }, {
//     firstName: "Filip",
//     secondName: "Modrý",
//     birth: 1989,
//     licencePlate: "2EP6328",
//     address: "Stevardská 38",
//     city: "České Budějovice"
// }]


// let filters = ""

// function Crim(ourCrim, tryToFind){
   
//     let arrRes = ourCrim.filter(function(sus){
//         return sus.licencePlate.toLowerCase().includes(tryToFind.toLowerCase())
//     })
    
//     document.querySelector("#criminal").innerHTML = ""

//     arrRes.forEach(element => {
//         let paragraph = document.createElement("p")
//         paragraph.textContent = `Name: ${element.firstName} ${element.secondName}`
        
//         document.querySelector("#criminal").appendChild(paragraph)
//     });
// }


// let licencePlate = document.querySelector("#SPZ")
// licencePlate.addEventListener("input", function(event){
//     filters = event.target.value
//     Crim(criminals, filters)
// })

// document.querySelector("#test").addEventListener("submit", function(event){
//     event.preventDefault()
    
//     console.log(event.target.elements.name.value)


//     let newP = document.createElement("p")
//     newP.textContent = event.target.elements.name.value
//     document.querySelector("#from_form").appendChild(newP)

//     event.target.elements.name.value = ""

// })



// document.querySelector("#test").addEventListener("submit", function(event){

//     event.preventDefault()
    

//     let newP = document.createElement("p")
//     newP.innerHTML = `Name: ${event.target.elements.name.value} <br> Secondname: ${event.target.elements.Secondname.value}<br> Email: ${event.target.elements.email.value}`
//     document.querySelector("#from_form").appendChild(newP)
    

//     event.target.elements.name.value = ""
//     event.target.elements.Secondname.value = ""
//     event.target.elements.email.value = ""

// })


// document.querySelector("#my_checkbox").addEventListener("change", function(event) {
//     console.log(event.target.checked)
// })


// document.querySelector("form").addEventListener("submit", function(e){
//     e.preventDefault()
// })

// let count = 0

// document.querySelector("form").addEventListener("submit", function(e){
//     e.preventDefault()
    

//     count++
//     let input = document.createElement("input")
//     input.type = "checkbox"
//     input.id = `check_${count}`
//     document.querySelector("#tasks").appendChild(input)


//     let label = document.createElement("label")
//     label.innerHTML = `${e.target.elements.task.value}<br>`
//     label.setAttribute("for", `check_${count}`)
//     // console.log(label)
//     document.querySelector("#tasks").appendChild(label)

//     e.target.elements.task.value = ""
// })


// document.querySelector("#my_sel").addEventListener("change", function(e){
//     console.log(e.target.value)
// })


// document.querySelector("body").addEventListener("keydown", function(e){
//     console.log(e.key)
// })

// let heading = document.querySelector("h1")

// heading.addEventListener("mouseenter", function(e){
//     heading.style.color = "blue"
// })

// heading.addEventListener("mouseleave", function(e){
//     heading.style.color = "green"
// })


// heading.style.fontWeight = 300
// heading.style.fontSize = "40px"

// heading.style.display = "none"



// let div = document.querySelector(".square")

// let newLeft = null
// let newTop = null

// document.querySelector("body").addEventListener("keydown", function(e){
//     if(e.key == "ArrowLeft") {
//         newLeft -= 30
//         div.style.left = newLeft + "px"
//     }
//     else if(e.key == "ArrowRight"){ 
//         newLeft += 30
//         div.style.left = newLeft + "px"
//     }
//     else if(e.key == "ArrowUp"){
//         newTop -= 30
//         div.style.top = newTop + "px"
//     } 
//     else if(e.key == "ArrowDown"){
//         newTop += 30
//         div.style.top = newTop + "px"
//     }
// })


// let heading = document.querySelector("h1")

// console.log(getComputedStyle(heading).color) 


// document.querySelector("form").addEventListener("submit", function(e){
//     e.preventDefault()
    
//     document.querySelector("body").style.background = e.target.elements.color.value
//     e.target.elements.color.value = ""
// })


// window.addEventListener("scroll", function(e){
//     let scrollable = document.documentElement.scrollHeight - window.innerHeight
//     let scrolled = this.window.scrollY

//     console.log(scrollable)
//     console.log(scrolled)

//     if(Math.floor(scrolled) == scrollable){
//         this.alert("You are at the bottom of the page")
//     }
     
// })
/******************************************/
//               button up                //
/******************************************/
// window.addEventListener("scroll", function(e){
//     let scrollable = document.documentElement.scrollHeight - window.innerHeight
//     let scrolled = this.window.scrollY


//     if(Math.ceil(scrolled) > 300){
//         let toTop = document.querySelector(".top_page")
//         toTop.style.display = "block"

//         toTop.addEventListener("click", function(e){
//             toTop.style.display = "none"
//         })
//     }
// })

let home = document.querySelector(".home")
let scroll_home = document.querySelector(".scroll_home").offsetTop

console.log(scroll_home)

home.addEventListener("click", function(){
    window.scrollTo({
        top: scroll_home,
        behavior: "smooth"
    })
})