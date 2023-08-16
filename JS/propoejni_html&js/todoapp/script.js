let ToDo = [{
    text: "Vynest kos",
    finished: false
},{
    text: "Nakoupit",
    finished: true
},{
    text: "Uklidit",
    finished: false
},{
    text: "Pes",
    finished: true
},{
    text: "Kocka",
    finished: false
}]

let x = 0
ToDo.forEach(element => {
    if(!element.finished){
        x++
        const newTTD = document.createElement("p")
        newTTD.textContent = element.text
        document.querySelector("#toDos").appendChild(newTTD)
    }
});
const num = document.createElement("p")
num.textContent = `Počet úkolů k dokončení: ${x}`
document.querySelector("#toDosLeft").appendChild(num)

// document.querySelector(".btn").addEventListener("click", function(event) {
   
// })

function renderToDos(list, ourInput) {
    let result = list.filter(function(one){
        return one.text.toLowerCase().includes(ourInput.toLowerCase())
    })

    let leftToDos = result.filter(function(one){
        return one.finished === false
    })


    document.querySelector("#toDosLeft").innerHTML = ""
    let newP = document.createElement("p")
    newP.textContent = `Počet úkolů k dokončení: ${leftToDos.length}`
    document.querySelector("#toDosLeft").appendChild(newP)

    document.querySelector("#toDos").innerHTML = ""

    result.forEach(element => {
        let par = document.createElement("p")
        par.textContent = element.text
        document.querySelector("#toDos").appendChild(par)
    });
}


let input_text = ""

let search_text = document.querySelector("#search")
search_text.addEventListener("input", function(event){
    input_text = event.target.value
    renderToDos(ToDo, input_text)
})