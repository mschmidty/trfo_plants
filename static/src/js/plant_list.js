// let markup;


// async function getPlants(query){
//   //let url = '{% url "plants:family_api" %}'
//   let url = '/plants/family_api'
//   //The below checks to see if you are on url /plants/  if you are it adjusts the urls below in `markup`
//   let pageUrl = window.location.pathname
//   let linkPath = "plants/";
//   if(pageUrl == '/plants/'){
//     linkPath = ""
//   }
//   const response = await fetch(url)
//   const jsonData = await response.json()
//   let species = await jsonData.species
//   if(query === "family"){
//     let groupedData = species.reduce((groups, line) => {
//       //if(line.family__family){
//         groups[line.family__family] = groups[line.family__family] || []
//         groups[line.family__family].push({
//           sci_name: line.genus + " " + line.species,
//           id: line.id,
//           image: line.image
//         })
//       //}
//       return groups
//     }, {})
//     function sortByKey(jsObj){
//         var sortedArray = [];

//         // Push each JSON Object entry in array by [key, value]
//         for(var i in jsObj)
//         {
//             sortedArray.push([i, jsObj[i]]);
//         }

//         // Run native sort function and returns sorted array.
//         return sortedArray.sort();
//     }
//     groupedData = sortByKey(groupedData)
//     markup = '<div class="flex-grid lrg-2 content-wrapper">'
//     for(let key in groupedData){
//       markup += `
//           <div class="family-list flex-grid-item">
//               <h2>${groupedData[key][0]}</h2>
//               <ul>
//                 ${groupedData[key][1].map(data => `<li><a href="${linkPath + data.id}">${data.sci_name}</a></li>`).join('')}
//               </ul>
//           </div>
//       `
//     }
//     markup += "</div>"

//   }else if(query === "commonName"){
//     species = species.sort((a,b)=>{
//       if(a.common_name != null & b.common_name !=null){
//         let a1 = a.common_name.toLowerCase();
//         let b1 = b.common_name.toLowerCase();
//         return a1<b1 ?-1:a1> b1? 1 :0;
//       }
//     })
//     markup = `
//       <ul class = "plant-list flex-grid lrg-3">
//         ${species.map(data => `<li class = "common_name flex-grid-item"><a href="${linkPath + data.id}">${data.common_name}</a></li>`).join('')}
//       </ul>
//     `
//   }else if(query==="symbol"){
//     markup = `
//       <ul class = "plant-list flex-grid lrg-3">
//         ${species.map(data => `<li class = "common_name flex-grid-item"><a href="${linkPath + data.id}">${data.symbol}</a></li>`).join('')}
//       </ul>
//     `
//   }else{
//     markup = `
//       <ul class = "plant-list flex-grid lrg-3">
//         ${species.map(data => `<li class = flex-grid-item><a href="${linkPath + data.id}">${data.genus + " " + data.species}</a></li>`).join('')}
//       </ul>
//     `
//   }
//   document.getElementById("plants-list").innerHTML = markup
// }
// getPlants("family");
// document.querySelectorAll(".sort-select").forEach(function(button){
//   button.addEventListener('click', function(event){
//     event.preventDefault();
//     let queryId = this.getAttribute('value');
//     getPlants(queryId)
//   }, false)
// })