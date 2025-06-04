$(document).ready(function () {
    eel.neuvela();
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
});
    // var siriWave = new SiriWave({
    //     container: document.getElementById("siri-container"),
    //     width: 800,
    //     height: 200,
    //     style: "ios9",
    //     amplitude: "5",
    //     speed: "0.22",
    //     frequency: "5",
    //     autostart: true,
    //     pixelDepth: 0.02,
    //     lerpSpeed: 1,
    // });
    $('.siri-message').textillate({
        loop: true,
        sequence: true,
        in: {
            effect: "flip",
            sync: true,
        },
        out: {
            effect: "rollOut",
            sync: true,
        },
    });
    //mic button view
    $("#Micbtn").click(function () {
        eel.playAssistantSound(); 
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        $("#closebtn").attr("hidden", false);
        eel.speak();
        eel.allcommand()();
        
    });
    $("#closebtn").click(function () {
        eel.playAssistantSound(); 
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        $("#closebtn").attr("hidden", true);
    });
    function doc_keyup(e) {
        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            $("#bot").attr("hidden", true);
            $("#studbot").attr("hidden", true);
            $("#docbot").attr("hidden", true);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", true);
            eel.allcommand()();
        }
    };
    document.addEventListener('keyup', doc_keyup, false);
    function playassistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            $("#closebtn").attr("hidden", false);
            eel.allcommand(message);
            $("#chatbox").val("");
            $("#Micbtn").attr("hidden", false);
            $("#Sendbtn").attr("hidden", true);
            
        }
        
    };
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#Micbtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else {
            $("#Micbtn").attr("hidden", true);
            $("#Sendbtn").attr("hidden", false);
        }
        
    };
    $("#chatbox").keyup(function () { 
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });
    $("#SendButton").click(function () { 
        let message = $("#chatbox").val();
        playassistant(message)
        
    });
    $("#chatbox").keypress(function (e) { 
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val();
            playassistant(message);
        }
    });
    $("#eco-mode").click(function () { 
        eel.playAssistantSound();
        $("#studbot").attr("hidden", true);
        $("#bot").attr("hidden", false);
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", true);
        $("#docbot").attr("hidden", true);
        $("#brotherbot").attr("hidden", true);
    });
    $("#friend").click(function () { 
        eel.playAssistantSound()
        $("#studbot").attr("hidden", true);
        $("#bot").attr("hidden", true);
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        $("#docbot").attr("hidden", true);
        $("#brotherbot").attr("hidden", true);
    });
    $("#stud-mode").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", true);
        $("#studbot").attr("hidden", false);
        $("#bot").attr("hidden", true);
        $("#docbot").attr("hidden", true);
        $("#brotherbot").attr("hidden", true);
    });
    $("#doc-mode").click(function () { 
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", true);
        $("#docbot").attr("hidden", false);
        $("#studbot").attr("hidden", true);
        $("#bot").attr("hidden", true);
        $("#brotherbot").attr("hidden", true);
    });
    $("#brother").click(function () { 
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", true);
        $("#docbot").attr("hidden", true);
        $("#studbot").attr("hidden", true);
        $("#bot").attr("hidden", true);
        $("#brotherbot").attr("hidden", false);
    });
    function doc_key(e) {
        if (e.key === '6' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", true);
            $("#bot").attr("hidden", true);
            $("#studbot").attr("hidden", true);
            $("#docbot").attr("hidden", false);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", true);
            eel.allcommand()();
        }
    };
    document.addEventListener('keyup', doc_key, false);
    function doc_keydown(e) {
        if (e.key === '7' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", true);
            $("#bot").attr("hidden", true);
            $("#studbot").attr("hidden", true);
            $("#docbot").attr("hidden", true);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", false);
            eel.allcommand()();
        }
    };
    document.addEventListener('keyup', doc_keydown, false);
    function doc_keyleft(e) {
        if (e.key === '8' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", true);
            $("#bot").attr("hidden", true);
            $("#studbot").attr("hidden", false);
            $("#docbot").attr("hidden", true);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", true);
            eel.allcommand()();
        }
    };
    document.addEventListener('keyup', doc_keyleft, false);
    function doc_keyright(e) {
        if (e.key === '9' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", true);
            $("#bot").attr("hidden", false);
            $("#studbot").attr("hidden", true);
            $("#docbot").attr("hidden", true);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", true);
            eel.allcommand()();
        }
    };
    document.addEventListener('keyup', doc_keyright, false);
    function doc_keyside(e) {
        if (e.key === '0' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", false);
            $("#SiriWave").attr("hidden", true);
            $("#bot").attr("hidden", true);
            $("#studbot").attr("hidden", true);
            $("#docbot").attr("hidden", true);
            $("#closebtn").attr("hidden", false);
            $("#brotherbot").attr("hidden", true);
            eel.allcommand()();
        }
    };
});