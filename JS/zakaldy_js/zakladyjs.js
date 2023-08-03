// console.log("Ucime se Javascript")
// console.log("Lolololo")

// let fisrtName = "Matej"
// let job = "Data analytic"


// console.log("Ahoj jmenuji se " + fisrtName + " a pracuji jako " + job)


// let st1 = 68
// let st2 = 88
// let maxpoints = 100
// let st1name = "Carl"
// let st2name = "Barny"

// st1acc = st1/maxpoints * 100
// st2acc = st2/maxpoints * 100

// console.log(st1name + " dosahl " + st1 + "%.")
// console.log(st2name + " dosahl " + st2 + "%.")
// let age = 66
// let child = age < 18
// let adult = age >= 18
// let pensioner = age >= 65

// console.log("Dite: " + child)
// console.log("Dospěly: " + adult)
// console.log("Senior: " + pensioner)


// let age = 18

// if (age > 18) {
//     console.log("Dospely")
// }else if(age < 18 && age > 10){
//     console.log("LLLOLOLO")
// }else {
//     console.log("KKT")
// }


// let temp = 45

// if(temp <= 10){
//     console.log("Chladno")
// }else if(temp >= 10 && temp <= 25){
//     console.log("Teplo")
// }else{
//     console.log("Horko")
// }


// let prvni = "Prvni text"

// if(true){
//     console.log(prvni)
//     let druha = "Druhy text"
//     console.log(druha)
// }

// function naDruhou(x){
//     return x**2
// }

// console.log(naDruhou(4))

// function adultChecker(age) {
//     if(age >= 18) {
//         x = "dospely"
//         return x
//     }else{
//         x = "dite"
//         return x
//     }
// }
// x = adultChecker(18)
// if (x == "dospely") console.log(x + "\n" + "Muzes")
// else console.log(x + "\n" + "Nemuzes")

// function soucet(a, b) {
//     return a + b
// }

// console.log(soucet(10, 5))


// num1 = 1
// num2 = 6
// num3 = 8 

// function entrance(a, b, c) {
//     if(a !== num1 || b !== num2 || c !== num3){
//         console.log("Wrong pin. Try it again")
//     }

//     else console.log("You can go.")
// }


// entrance(1, 6, 8)



// let name = "Matej"
// let age = 20

// console.log(`Ahoj ja jsem ${name} a je mi ${age} let.`)


// let myBook = {
//     title: "Harry Potter",
//     author: "J. K. Rowling",
//     published: 1997
// }

// myBook.title = "Auta"
// console.log(myBook.title)



// let person1 = {
//     name: "Dominik",
//     age: "28",
//     city: "Teplice",
//     gender: "male"
// }

// let person2 = {
//     name: "Jan",
//     age: "30",
//     city: "Dubi",
//     gender: "male"
// }
// let person3 = {
//     name: "Dana",
//     age: "45",
//     city: "Bilina",
//     gender: "female"
// }


// console.log(`Jmenuje se ${person1.name}. Je mu ${person1.age} a pochazi z ${person1.city}.`)
// console.log(`Jmenuje se ${person2.name}. Je mu ${person2.age} a pochazi z ${person2.city}.`)
// console.log(`Jmenuje se ${person3.name}. Je mu ${person3.age} a pochazi z ${person3.city}.`)


// function res(person) {
//     if(person.gender == "male") {
//         console.log(`Jmenuje se ${person.name}. Je mu ${person.age} a pochazi z ${person.city}.`)
//     }
//     else console.log(`Jmenuje se ${person.name}. Je ji ${person.age} a pochazi z ${person.city}.`)
// }

// res(person1)
// res(person2)
// res(person3)



// let person1 = {
//     fName: "Matej",
//     sName: "Asamoah",
//     age: 35,
//     height: 185,
//     salary: 20000,
//     greet: function(){
//         console.log("Ahoj")
//     },
//     toWork: function(job){
//         return `I'm working as ${job}.`
//     }
// }


// person1.greet()
// let work = person1.toWork("programmer")
// console.log(work)


// let school = {
//     type: "high school",
//     street: "Cs. Dobrovlcu",
//     city: "Teplice",
//     capacity: "800",
//     open: function(){
//         console.log("School is open.")
//     },
//     closed: function(){
//         return "School is closed"
//     }
// }


// console.log(school.type, school.city)
// school.open()
// let clo = school.closed()
// console.log(clo)



// let person1 = {
//         fName: "Matej",
//         sName: "Asamoah",
//         age: 35,
//         greet: function(){
//             console.log(this.fName)
//         }
// }

// let person2 = {
//     fName: "Ludek",
//     sName: "Asamoah",
//     age: 25,
//     greet: function(){
//         console.log(this.fName)
//     }
// }


// person1.greet()
// person2.greet()

// let vlNa = false

// let school = {
//     type: "gymanzium",
//     street: "Cs. Dobrovlcu",
//     city: "Teplice",
//     capacity: "800",
//     open: function(){
//         console.log(`Skola ${this.type} ${this.city} je otevrena.`)
//     },
//     closed: function(){
//         console.log(`Skola ${this.type} ${this.city} je zavrena.`)
//     }
// }


// if(vlNa) school.closed()
// else school.open()


// fName = "David"
// len = fName.length
// console.log(len)

// console.log(fName.toUpperCase())
// console.log(fName.includes("david"))
// console.log(fName.trim())



// let password = "Lojza1234jekral"
// let lenpass = password.length

// if(lenpass > 13)console.log("Velmi silne heslo")
// else if(lenpass <= 13 && lenpass >= 8) console.log("Silne heslo")
// else console.log("Slaboch")


// if(password.includes("1234")) console.log("Heslo nesmi obsahovat 1234.")
// else console.log("Heslo je v poradku.")



// let num =  3.1438
// console.log(num.toFixed(1))
// console.log(Math.round(num))
// console.log(Math.floor(num))
// console.log(Math.ceil(num))

// console.log(Math.random())
// console.log(Math.ceil(Math.random()*10))


// let min = 1
// let max = 6
// console.log(Math.floor(Math.random() * (max - min + 1)) + min)


// let max = 6
// let min = 1
// let num1 =  Math.floor(Math.random() * (max - min + 1)) + min
// let num2 =  Math.floor(Math.random() * (max - min + 1)) + min
// let num3 =  Math.floor(Math.random() * (max - min + 1)) + min
// let num4 =  Math.floor(Math.random() * (max - min + 1)) + min
// let num5 =  Math.floor(Math.random() * (max - min + 1)) + min
// let num6 =  Math.floor(Math.random() * (max - min + 1)) + min

// let sum = num1 + num2 + num3 + num4 + num5 + num6

// if(sum >= 25) console.log("Vyhjaal")
// else console.log("try it again")

// console.log(`Celkovy soucet je ${sum}`)

// console.log("%c lololololo", "color: #b90000; background: #fff")


// let nums = [1, 5, 6, 7]

// console.log(nums[0])


// let passwords = ["abcd8811", "kovy1188", "lolovyhjal"]
// let randint = Math.ceil(Math.random()*3)
// console.log(randint)
// console.log(passwords[randint-1])


// let test = ["test1", "test2", "test3"]
// test.push("test4")
// test.pop()
// test.unshift("test")
// test.shift("test")
// console.log(test)

// test.splice(1,2)
// console.log(test)
// test.splice(2, 0, "testx")
// console.log(test)

// let array = []
// for (let index = 0; index < 3; index++) {
//     array[index] = prompt("Zadej jmeno");
    
// }
// for (let index = 0; index < 3; index++) {
//     let name = prompt("Zadej jmeno");
//     array.unshift(name)
// }
// console.log(array)



// let x = ["a", "b", "c", "d"]

// x.forEach(element => {
//     console.log("x")
// });


// x.forEach(function(word){
//     console.log(word)
// })


// x.forEach(function(element, index) {
//     console.log(element, index)
// });



// let toDo = ["pes", "kecup", "pokoj", "svacina"]

// toDo.forEach(function(element, index) {
//     console.log(`${index+1}. ${element}`)
// });


// let toDo = ["pes", "kecup", "pokoj", "svacina"]

// for (let i = 0; i < toDo.length; i++) {
//     console.log(`${i+1}. ${toDo[i]}`)
// }

// let nums = []

// for (let i = 0; i < 5; i++) {
//     nums.push(i)
// }

// console.log(nums)


// let employess = ["David", "Jana", "Marek"]
// console.log(employess.indexOf("David"))
// console.log(employess.indexOf("Davi"))



// let books = [{
//     title: "Harry potter kamen",
//     author: "J.K. Rowlingova",
//     published: 1997
// },{
//     title: "Harry potter komnata",
//     author: "J.K. Rowlingova",
//     published: 1998
// },{
//     title: "Harry potter vezen",
//     author: "J.K. Rowlingova",
//     published: 1999
// }]

// let arr = [4, 1, 2, 38, 7]

// let result = arr.findIndex(function(num) {
//     return num > 10
// })

// console.log(result)


// let index = books.findIndex(function(onebook){
//     return onebook.published === 1998
// })

// console.log(index)


// let criminals = [{
//     firstName: "Martin",
//     secondName: "Zelený",
//     birth: 1985,
//     address: "U sloupů 16",
//     city: "České Budějovice"
// }, {
//     firstName: "Jana",
//     secondName: "Růžová",
//     birth: 1996,
//     address: "Malská 29",
//     city: "České Budějovice"
// }, {
//     firstName: "Filip",
//     secondName: "Modrý",
//     birth: 1989,
//     address: "Stevardská 38",
//     city: "České Budějovice"
// }]


// let index = criminals.findIndex(function(name){
//     let pName = prompt("Zadej jmeno")
//     return name.firstName === pName
// })

// console.log(`Jmeno: ${criminals[index].firstName}\nPrijmeni: ${criminals[index].secondName}\nDatum narozeni: ${criminals[index].birth}`)




// let books = [{
//     title: "Harry potter kamen",
//     author: "J.K. Rowlingova",
//     published: 1997
// },{
//     title: "Harry potter komnata",
//     author: "J.K. Rowlingova",
//     published: 1998
// },{
//     title: "Harry potter vezen",
//     author: "J.K. Rowlingova",
//     published: 1999
// }]


// let arr = [1, 3, 20, 5, 8]

// let res = arr.find(function(num){
//     return num > 4
// })

// console.log(res)

// let res = books.find(function(onebook) {
//     if(onebook.published === 1999) return onebook
// })

// console.log(res.title)

// let arr = [1, 3, 20, 5, 8]

// let arrRes = arr.filter(function(num){
//     let find = num >= 5
//     return find
// })

// console.log(arrRes)



// let arrNames = ["David", "Anna", "Jana", "Nada"]

// let arrayRes = arrNames.filter(function(name){
//     let find = name.toLowerCase().includes("na")
//     return find
// })

// console.log(arrayRes)


// let books = [{
//     title: "Harry potter kamen",
//     author: "J.K. Rowlingova",
//     published: 1997
// },{
//     title: "Harry potter komnata",
//     author: "J.K. Rowlingova",
//     published: 1998
// },{
//     title: "Harry potter vezen",
//     author: "J.K. Rowlingova",
//     published: 1999
// },{
//     title: "Harry Row",
//     author: "J.K.",
//     published: 1999
// }]


// let res2 = books.filter(function(book){
//     let x = book.author.toLowerCase().includes("row")
//     let y = book.title.toLowerCase().includes("row")
//     return x || y
// })

// res2.forEach(function(book){
//     console.log(book.title)
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

// let spz = prompt("Zadej spz kriminalnika")

// let sus = criminals.filter(function(witness){
//     let x = witness.licencePlate.toLowerCase().includes(spz)
//     return x
// })

// sus.forEach(function(i){
//     console.log(`Jmeno: ${i.firstName}`)
//     console.log(`Prijmeni: ${i.secondName}`)
//     console.log(`Datum nar: ${i.birth}`)
//     console.log(`SPZ: ${i.licencePlate}`)
//     console.log(`Adresa: ${i.address}`)
//     console.log(`Mesto: ${i.city}`)
//     console.log("\n")
// })




let names = ["Anna", "Crambora", "Becile"]

names.sort()

console.log(names)

let nums = [1, 15, 4, 6, 3, 7, 5]

nums.sort()

console.log(nums)


let books = [{
    title: "Harry Potter a kámen mudrců",
    author: "J. K. Rowlingová",
    published: 1997
}, {
    title: "Harry Potter a vězeň z Azkabanu",
    author: "J. K. Rowlingová",
    published: 1999
}, {
    title: "Harry Potter a Tajemná komnata",
    author: "J. K. Rowlingová",
    published: 1998
}]

function sortArr(arrBooks) {
    arrBooks.sort(function(a, b) {
        if(a.title.toLowerCase() < b.title.toLowerCase()){
            return -1
        }else if(a.title.toLowerCase() > b.title.toLowerCase()){
            return 1
        }else return 0
        
    })
}

sortArr(books)
console.log(books)