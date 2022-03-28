function verify() {
    var num = document.querySelector('input#num1')
    var box = document.querySelector('select#seltab')
    
    if (num.value.length == 0) {
        alert('[ERRO]Insira um valor acima')
    } else {
        
        var n = Number(num.value)
        box.innerHTML = ''
       
        
        for (let c = 0; c <= 10; c++ ) {
        let res = document.createElement('option')
        res.text += `${n} x ${c} = ${n*c}`
        box.appendChild(res)
        
            
        }
    

    }
}