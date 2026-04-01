fetch("URL")
.then(res => res.json())
.then(data => {

   document.querySelector("#character").innerText = data.name

})
