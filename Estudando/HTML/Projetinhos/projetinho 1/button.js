let num = document.querySelector('input#num')
let res = document.querySelector('div#res')
let btn = document.addEventListener('keypress', function(e) {
    if(e.key == 'Enter') {
        var btn =document.querySelector('input#but')
        btn.click()
    }
})
function calcular(){
    let i = Number(num.value)
    let med = document.getElementsByName('radmedida')
    res.innerHTML = ''
    if(num.value.length == 0) {
        alert('Infome um valor')
    }
    else if (med[0].checked) {
        res.innerHTML += `${i * 1000}mm`
    } else if (med[1].checked) {
        res.innerHTML += `${i * 100}cm`
    } else if (med[2].checked) {
        res.innerHTML = `${i * 10}dm`
    }else if (med[3].checked) {
        res.innerHTML += `${i / 1000}km`
    } else if (med[4].checked) {
        res.innerHTML += `${i / 100}hm`
    } else if (med[5].checked) {
        res.innerHTML = `${i / 10}dam`
}

}
