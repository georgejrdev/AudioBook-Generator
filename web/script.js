document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('pdf-file');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file!');
        return;
    }

    const formData = new FormData();
    formData.append('pdf', file);

    try {
        setDisplayDivLoading("flex")

        const response = await fetch('http://127.0.0.1:3030/generateAudio', {
            method: 'POST',
            body: formData
        });

        setDisplayDivLoading("none")
        
        if (!response.ok) {
            throw new Error('Upload failed!');
        }

        const blob = await response.blob();
        const url = URL.createObjectURL(blob); 
        const a = document.createElement('a');  
        a.href = url;
        a.download = 'audio.mp3'; 
        a.style.display = 'none';  
        document.body.appendChild(a); 
        a.click();
        URL.revokeObjectURL(url);  
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to upload file.');
    }
});


function setDisplayDivLoading(display){
    divLoading = document.getElementById("loading")
    divLoading.style.display = display
}