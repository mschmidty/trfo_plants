const url = '/plants/family_api'

const plants = [];

fetch(url)
  .then(data=>data.json())
  .then(data=>{
    plants.push(...data.species)
    return data.species
  })
  .then(data => {
      const fullGroupedArray = familyKeyArray(data);
      const sortedPlants = sortByKey(fullGroupedArray);
      displayMatches(sortedPlants);
  })


function findMatches(wordToMatch, plants){
  return plants.filter(search=>{
    const regex = new RegExp(wordToMatch, 'gi');
    return search.family__family.match(regex) || search.genus.match(regex) || search.species.match(regex) 
  })
}
function familyKeyArray(plants){
  const groupedData = plants.reduce((groups, line) => {
    //if(line.family__family){
      groups[line.family__family] = groups[line.family__family] || []
      groups[line.family__family].push({
        sci_name: line.genus + " " + line.species,
        id: line.id,
        image: line.image,
        common_name: line.common_name,
        symbol: line.symbol
      })
    //}
    return groups
  }, {})
  return groupedData
}

function sortByKey(jsObj){
  return Object.keys(jsObj).sort().reduce(function (result, key) {
    result[key] = jsObj[key];
    return result;
  }, {});
  
}


function displayMatches(){
  const matchArray = findMatches(this.value, plants)
  const matchArrayGrouped = familyKeyArray(matchArray)
  const matchArrayFiltered = sortByKey(matchArrayGrouped)
  displayPlants(matchArrayFiltered);
}

function displayPlants(groupedArray){
  let markup2 = '<div>'
  for(let key of Object.keys(groupedArray)){
    markup2 += `
          <div class = "family-list">
              <h2>${key}</h2>
              <ul class = "card-list flex-grid lrg-3">
                ${groupedArray[key].map(data => `
                  <li class="species-card flex-grid-item">
                    <a href="../plants/${data.id}">
                      <div class="image-wrapper">
                        <img src="/media/${data.image}">
                      </div>
                      <div class="text-wrapper">
                      <h3>${data.sci_name}</h3>
                      <span class="extra-info">
                        <p class="common-name">${data.common_name}</p>
                        <p class="symbol">${data.symbol}</p>
                      </span>
                      </div>
                    </a>
                  </li>
                  `).join('')}
              </ul>
          </div>
      `
  }
  markup2 += '</div>'
  suggestions.innerHTML = markup2;
}

const searchInput = document.querySelector('.search');
const suggestions = document.querySelector('#plants-list')

searchInput.addEventListener('keyup', displayMatches)