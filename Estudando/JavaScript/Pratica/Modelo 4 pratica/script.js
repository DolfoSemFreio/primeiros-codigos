function verify() {
    let num = document.querySelector('input#num1')
    let box = document.querySelector('select#seltab')
    if (num.value.length == 0) {
        alert('[ERRO]Preencha os campos e tente novamente')
    } else {
        let n1 = Number(num.value)
        let c = 1
        box.innerHTML = ''
        while (c <= 50) {
            let res = document.createElement('option')
            res.text = `${n1} x ${c} = ${n1*c}`
            res.value = `tab${c}`
            box.appendChild(res)
            c++
            

        }
    }

}