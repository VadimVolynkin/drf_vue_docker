<template>
    <div>
        <v-col cols="8">
            <v-container class="max-width">
                <v-pagination
                    v-model="page"
                    class="my-4"
                    :length="parseInt(carsCount / cars.length)"
                    total-visible="12"
                    @input="fetchCars(baseUrl + page)"
                    @next="fetchCars(nextPage)"
                    @prev="fetchCars(previousPage)"
                ></v-pagination>
            </v-container>
        </v-col>

        <div>
            <h1>Cars count: {{ this.carsCount }}</h1>
        </div>
        <input placeholder="vendor" v-model="currentCar.vendor" />
        <input placeholder="model" v-model="currentCar.model" />
        <input placeholder="year" v-model.number="currentCar.year" />
        <input placeholder="volume" v-model.number="currentCar.volume" />
        <div v-if="isUpdating">
            <button @click="confirmUpdateCar(idUpdatingCar)">Confirm</button>
            <button @click="cancelUpdateCar()">Cancel</button>
        </div>
        <div v-else>
            <button @click="createCar()">Create</button>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Vendor</th>
                    <th>Model</th>
                    <th>Year</th>
                    <th>Volume</th>
                    <th>Remove</th>
                    <th>Update</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="car in cars" :key="car.id">
                    <td>{{ car.vendor }}</td>
                    <td>
                        <a :href="car.id" @click="goTo(car.id)">{{
                            car.model
                        }}</a>
                    </td>
                    <td>{{ car.year }}</td>
                    <td>{{ car.volume }}</td>
                    <td><button @click="removeCar(car)">Remove</button></td>
                    <td><button @click="updateCar(car)">Update</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Home",
    data() {
        return {
            cars: [],
            currentCar: {},
            carsCount: Number,
            page: 1,
            previousPage: null,
            nextPage: null,
            baseUrl: "http://127.0.0.1:8000/api/cars/?page=",
            isUpdating: false,
            idUpdatingCar: null,
        };
    },

    async created() {
        // get cars from backend in the first time
        this.fetchCars();
    },

    methods: {
        async fetchCars(url = "http://127.0.0.1:8000/api/cars/") {
            await axios
                .get(url)
                .then((response) => {
                    const { results, count, next, previous } = response.data;
                    this.cars = results;
                    this.carsCount = count;
                    this.nextPage = next;
                    this.previousPage = previous;
                })
                .catch((error) => alert(error));
        },

        async createCar(url = "http://127.0.0.1:8000/api/cars/") {
            await axios
                .post(url, this.currentCar)
                .then(() => {
                    // clear createform on frontend after successful POST
                    this.currentCar = {};
                    // get cars with new added car from backend after backend-validation
                    this.fetchCars();
                })
                .catch((error) => alert(error));
        },

        async updateCar(car) {
            const { id } = car;
            this.idUpdatingCar = id;
            const url = `http://127.0.0.1:8000/api/cars/${id}/`;
            await axios
                .get(url)
                .then((response) => {
                    this.isUpdating = true;
                    this.currentCar = response.data;
                })
                .catch((error) => alert(error));
        },

        // confirm update changes and clear form
        async confirmUpdateCar(idUpdatingCar) {
            const url = `http://127.0.0.1:8000/api/cars/${idUpdatingCar}/`;
            await axios
                .put(url, this.currentCar)
                .then(() => {
                    // get cars with updated car from backend after backend-validation
                    this.fetchCars();
                })
                .catch((error) => alert(error));
            // switch updating status
            this.isUpdating = false;
            // clear updateform on frontend after successful PUT
            this.currentCar = {};
        },

        // cancel update process and clear form
        async cancelUpdateCar() {
            this.idUpdatingCar = null;
            this.isUpdating = false;
            this.currentCar = {};
        },

        async removeCar(car) {
            const { id } = car;
            const url = `http://127.0.0.1:8000/api/cars/${id}/`;
            await axios
                .delete(url)
                .then(() => {
                    // get cars without removed car from backend
                    this.fetchCars();
                })
                .catch((error) => alert(error));
        },

        // go to Car page
        async goTo(id) {
            this.$router.push({ name: "Car", params: { id: id } });
        },
    },
};
</script>



// TODO where to include axios.get? in created or mounted?
// TODO does need updateCar to reload or not?
// TODO validate create and update backend
// TODO validate create and update frontend
// TODO add sort in table
// TODO add filter in table
// TODO add search in table