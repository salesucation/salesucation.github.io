window.addEventListener('load', function () {
    const el = '#app';
    var $ = Dom7;

    const app = new Framework7({
        el,
        theme: 'md',
        darkMode: "auto",
        clicks: {
            externalLinks: 'a:not(.panel-open)',
        }

    })

    // create searchbar
    app.searchbar.create({
        el: '.searchbar',
        searchContainer: '.list-email',
        searchIn: '.item-title',
        on: {
            search(sb, query, previousQuery) {
                console.log(query, previousQuery);
            }
        }
    });
    //
    const oForm = document.querySelector("form");
    oForm.addEventListener("submit", function(){
        const url = new URL(location);
        url.searchParams.set("s", oForm.querySelector("input").value);
        history.pushState({}, "", url);
    })
    if(!this.localStorage.getItem("cookies_accepted")){
        this.localStorage.setItem("cookies_accepted", new Date().toLocaleString());
        const cookieMessage = app.sheet.create(
            {
                el: '.cookie-message'
            });
        $(".cookie-message .sheet-close").on("click", ()=>{
            cookieMessage.close();
        })
        cookieMessage.open();
    }
    if(this.navigator.userAgent.match(/Android/i)){
        this.document.querySelector(el).classList.add("android");
    }

});