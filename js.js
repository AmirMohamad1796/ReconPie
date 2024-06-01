const mlinks=document.querySelector("#menu__links");
const msubs=document.querySelector("#menu__subs");
const mstep3=document.querySelector("#menu__step3");
const mip=document.querySelector("#menu__ip");
const mports=document.querySelector("#menu__ports");
const mregex=document.querySelector("#menu__regex");
const mwhois=document.querySelector("#menu__whois");
const mwapp=document.querySelector("#menu__wapp");




// everydiv
const divlink=document.querySelector("#link-wrraper");
const divlinks=document.querySelector("#links-wrraper");
const divsubs=document.querySelector("#subs-wrraper");
const divstep3=document.querySelector("#step3-wrraper");
const divip=document.querySelector("#ips-wrraper");
const divport=document.querySelector("#ports-wrraper");
const divregex=document.querySelector("#regex-wrraper");
const divwhois=document.querySelector("#whois-wrraper");
const divwapp=document.querySelector("#wapp_wrraper");









let count_link=0;
mlinks.addEventListener("click",()=>{
    if(count_link==0){
        divlink.style.display="block";
        divlinks.style.display="block";

        count_link++;
    }else{
        count_link=0;
        divlink.style.display="none";
        divlinks.style.display="none";

    }

});




let count_subs=0;
msubs.addEventListener("click",()=>{
    if(count_subs==0){
        divsubs.style.display="block";

        count_subs++;
    }else{
        count_subs=0;
        divsubs.style.display="none";

    }
  
    

});
let count_step3=0;
mstep3.addEventListener("click",()=>{
    if(count_step3==0){
        divstep3.style.display="block";
        count_step3++;
    }else{
        count_step3=0;
        divstep3.style.display="none";


    }
  
    

});



let count_ip=0;
mip.addEventListener("click",()=>{
    if(count_ip==0){
        divip.style.display="block";


        count_ip++;
        which_step();
    }else{
        count_ip=0;
        divip.style.display="none";


    }
    

});


let count_port=0;
mports.addEventListener("click",()=>{
   
    if(count_port==0){
        divport.style.display="block";

        count_port++;
    }else{
        divport.style.display="none";
        count_port=0;

    }
  
    

});

let count_regex=0;
mregex.addEventListener("click",()=>{
    
    if(count_regex==0){
        divregex.style.display="block";

        count_regex++;
    }else{
        divregex.style.display="none";
        count_regex=0;

    }
  
    

});


let count_whois=0;
mwhois.addEventListener("click",()=>{
   
    if(count_whois==0){
        divwhois.style.display="block";

        count_whois++;
    }else{
        divwhois.style.display="none";
        count_whois=0;

    }
  
    

});

let count_wapp=0;
mwapp.addEventListener("click",()=>{
    
    if(count_wapp==0){
        divwapp.style.display="block";

        count_wapp++;
    }else{
        divwapp.style.display="none";
        count_wapp=0;

    }
  
    

});


////////////////////////////////////////////////////////////////////////////////

// function which_step(){
//     if(links==true){
//         divsubs.style.display="none";
//         divstep3.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//    else if(subs==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divstep3.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//    else if(thirdstep==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//     else if(ip==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divstep3.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//     else if(port==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divip.style.display="none";
//         divip.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//     else if(regex==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divip.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divwhois.style.display="none";
//         divwapp.style.display="none";
//     }
//     else if(whois==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divip.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwapp.style.display="none";
//     }
//     else if(wapp==true){
//         divlinks.style.display="none";
//         divlink.style.display="none";
//         divsubs.style.display="none";
//         divip.style.display="none";
//         divip.style.display="none";
//         divport.style.display="none";
//         divregex.style.display="none";
//         divwhois.style.display="none";
//     }
// }