document.getElementById("file-upload")
.addEventListener('change', e =>{
    const form = new FormData(document.getElementById("upload_form"));
    console.log({form})
    fetch('/upload', {
        method : 'post', 
        body : form
    })
})