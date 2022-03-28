function enter() {
    let num = document.querySelector('input#num1')
    let box = document.querySelector('select#seltab')
    
    
    if (num.value.length == 0) {
        alert('Please select a number')
    } else {
        let n1 = Number(num.value)
        let c = 1
        box.innerHTML = ''
        while (c <= 20) {
            let b1 = document.createElement('option')
            b1.text = `${n1} x ${c} = ${n1*c}`
            b1.value = `tab${c}`
            box.appendChild(b1)
            c++
            
            

            
        }
        
    }
}