function verify() {
    let numb = document.querySelector('input#num1')
    let box = document.querySelector('select#seltab')

    if (numb.value.length == 0) {
        alert('informe um valor primeiro')
    } else {
        let n1 = Number(numb.value)
        let c = 1
        box.innerHTML = ''
        
        do {
             let box1 = document.createElement('option')
            box1.text += (`${n1} / ${c} = ${n1/c}`)
            box.appendChild(box1) 
            c++
            
        } while (c <= 1000)
        
    }
}