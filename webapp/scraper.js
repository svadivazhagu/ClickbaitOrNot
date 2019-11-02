/*
    @param filtered json containing the id of a video, and the link to thumbnail
    @returns 

*/

    function scraper() {
       var vids = document.querySelectorAll('#video-title');
        filtered_vids = {};

        for (let i = 0; i<vids.length; i++){
            let vid = {'title':vids[i]['innerText'], 'id':vids[i]['search'].slice(3)};
            filtered_vids.push(vid)
        }            
    }