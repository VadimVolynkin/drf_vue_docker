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
        <button @click="createCar()">Create</button>

        <table>
            <thead>
                <tr>
                    <th>Vendor</th>
                    <th>Model</th>
                    <th>Year</th>
                    <th>Volume</th>
                    <th>Remove</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="car in cars" :key="car.id">
                    <td>{{ car.vendor }}</td>
                    <td>{{ car.model }}</td>
                    <td>{{ car.year }}</td>
                    <td>{{ car.volume }}</td>
                    <td><button @click="removeCar(car)">Remove</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
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
        };
    },

    async created() {
        // get cars from backend in first time
        this.fetchCars();
    },

    methods: {
        // method GET cars from backend
        async fetchCars(url = "http://127.0.0.1:8000/api/cars/") {
            const response = await fetch(url);
            const { results, count, next, previous } = await response.json();
            this.cars = results;
            this.carsCount = count;
            this.nextPage = next;
            this.previousPage = previous;
        },

        // method POST new car
        async createCar() {
            const response = await fetch("http://127.0.0.1:8000/api/cars/", {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(this.currentCar),
            });

            // check status after POST and show alert with response data
            if (response.status !== 201) {
                alert(JSON.stringify(await response.json(), null, 2));
            } else {
                // clear createform on frontend after successful POST
                this.currentCar = {};
            }

            // get cars with new added car from backend after backend-validation
            await this.fetchCars();
        },

        // method remove car
        async removeCar(car) {
            const { id } = car;
            const response = await fetch(
                `http://127.0.0.1:8000/api/cars/${id}/`,
                {
                    method: "DELETE",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                    },
                }
            );

            // check status after DELETE
            if (response.status !== 204) {
                alert(JSON.stringify(await response.json(), null, 2));
            }

            // get cars without removed car from backend
            await this.fetchCars();
        },
    },
};
</script>



// TODO use axios
// TODO create update method
// TODO create Item page with CRUD
// TODO validate create and update backend
// TODO validate create and update frontend