<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Vendor</th>
          <th>Model</th>
          <th>Year</th>
          <th>Volume</th>
      </tr>
      </thead>
      <tbody>
        <tr v-for="car in cars" :key="car.id">
          <td>{{ car.vendor }}</td>
          <td>{{ car.model }}</td>
          <td>{{ car.year }}</td>
          <td>{{ car.volume }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      cars:[],
    }
  },
  async created() {
    const response = await fetch('http://127.0.0.1:8000/api/cars/')
    this.cars = await response.json()
  },
  components: {
  }
}
</script>
