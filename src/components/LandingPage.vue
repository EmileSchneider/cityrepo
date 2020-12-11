<template>
<div class="landingPage">
  <b-container>
    <b-row>
      <b-col>
	<h1>{{ firstName + ' ' + lastName }}</h1>
	<p>{{ description }}</p>
      </b-col>
      <b-col>
	<div>
	  <b-card
	    img-src="https://picsum.photos/600/300/?image=25"
	    img-alt="Image"
	    img-top
	    tag="article"
	    class="mb-2"
	    >  
	    <b-button href="#" variant="primary">githhub Go somewhere</b-button>
	</b-card>
      </div>
	</b-col>
    </b-row>
    <b-row>
      <b-col>
	<b-button class="bur" variant="danger">CV</b-button>
	<br />
	<b-button class="bur" variant="success">Portfoilio</b-button>
      </b-col>
      <b-col>
      </b-col>
      
    </b-row>
    
    </b-container>
  </div>
</template>

<script>
    import axios from 'axios';
    export default {
      name: 'LandingPage',
      props: {},
      data: function() {
        return {
          firstName: "Emiule",
          lastName: "Schneider",
          description: "LOREM Isdifnaosjdfbkasdf sadfbsd fueiqdgp "
        }
      },
      mounted: function() {
        axios.get('http://localhost:8000/landingpage')
        .then(res => {
          this.firstName = res.data.firstName,
          this.lastName = res.data.lastName
        })
        .catch(err => console.log(err))
      }
    } 
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bur {
    width: 100%;
    margin: 2em;
    height: 5em;
}

</style>
