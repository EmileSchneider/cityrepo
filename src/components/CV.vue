<template>
<div class="CV">
  <b-container>
    <h1>CV</h1>
    <b-row>
      
      <b-col>
	<h1>Work Expierience</h1>
	<b-row v-bind:key="w.description" v-for="w in work">
	  <div class="Work" style="box-shadow:0 0 0.5em rgba(0,0,0,0.6); padding: 0.5em; width:100%; margin:1em;">
	    <h2>{{w.employer}}</h2>
	    <h4>{{w.duration}}</h4>
	    <p>{{w.work}}</p>
	  </div>
	</b-row>
      </b-col>
      <b-col>
	<h1>Education and Skills</h1>
      <b-row v-for="e in education">
	<div style="box-shadow:0 0 0.5em rgba(0,0,0,0.5); padding: 0.5em; width:100%; margin:1em;">
	  <h2>{{e.institution}}</h2>
	  <h4>{{e.description}}</h4>
	</div>
      </b-row>
      </b-col>
    </b-row>
  </b-container>
  </div>
</template>

<script>
import axios from 'axios';
    export default {
      name: 'CV',
      props: {},
      data: function() {
        return {
		  work: [],
		  education: []
        }
      },
      mounted: function() {
        axios.get('http://localhost:8000/cv')
        .then(res => {
      this.work = res.data[0];
      this.education = res.data[1];
		  console.log(res.data)
        })
        .catch(err => console.log(err))
      }
    } 
</script>
