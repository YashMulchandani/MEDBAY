var updateBtns = document.getElementsByClassName('update-cart')

for(var i =0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click' , function()
      var productId = this.dataset.products
      var action = this.dataset.action
      console.Log('productId:', productId, 'action:' , action)

      console.Log('USER:', user);
      if(user ==='AnonymousUser'){
          console.Log('not logged in')
      }else{
          updateUserOrder(productId, action)
      }
  })
}

function updateUserOrder(productId, action){
  console.Log('user is logged in, sending data..')

  var url = '/update_item/'

  fetch(url, {
    method:'POST',
    headers:{
          'content-type':'application/json'
          'X-CSRFToken':csrftoken,
    },
    body:stringify({'productId':, productId, 'action':, action})
  })

  .then((response) =>{
    return response.json
  })

  .then((response) =>{
    console.Log('data:', data)
    location.reload()
  })
}
