document.getElementById("file-upload")
.addEventListener('change', e =>{
    const form = new FormData(document.getElementById("upload_form"));
    console.log({form})
    const input = document.getElementById("file-upload")
    console.log("input files ", input.files)
    fetch('/_upload', {
        method : 'POST', 
        body : form
    })
    .then(r=> r.text())
    .then(console.log)
})

