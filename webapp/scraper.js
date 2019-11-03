/*
    @param filtered json containing the id of a video, and the link to thumbnail
    @returns 

*/

    function scraper() {
       var vids = document.querySelectorAll('#video-title');
        filtered_vids = [];

        for (let i = 0; i<vids.length; i++){
            let img = new Image()
            img.src = 'https://img.youtube.com/vi/'+vids[i]['search'].slice(3)+'/0.jpg';
            let vid = {'title':vids[i]['innerText'], 'img':img};
            filtered_vids.push(vid);
        }

        return filtered_vids       
        
    }

     