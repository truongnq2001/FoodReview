function checkPhoto(img) 
{
    img = new Image()
    img.src = window.URL.createObjectURL(event.target.files[0])
    img.onload = () => {
        if(img.width <= 400 && img.height <= 400)
        {
            return True
        } 
        else
        {
            alert(`Ảnh bạn tải lên có định dạng ${img.width} x ${img.height}. Định dạng tối đa của ảnh đại diện là 400 x 400`);
            window.location = '/profile/'
        }                
    }
}