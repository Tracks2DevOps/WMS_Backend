<template>
  <div class="warehouseorders">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Shipping Inventory</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Orders</p>
              <ul class="menu-list">
                <li><a class="is-active">All Orders</a></li>
                <li><a>In Warehouse</a></li>
                <li><a>Shipped From Warehouse</a></li>
                <li><a>Pending Orders</a></li>
              </ul>
            </aside>
          </div>

          <div class="column is-15">
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="order in orders"
                v-bind:key="order.id"
              >
                <div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img src="http://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                    </figure>
                  </div>

                  <div class="card-content">
                    <div class="media">
                      <div class="media-content">
                        <p class="is-size-5">{{ order.title }}</p>
                      </div>
                    </div>
                  </div>

                  <div class="content">
                    <p>More placeholder text</p>

                    <a href="#">View</a>
                  </div>
                </div>
              </div>

            </div>
            <div class="column is-12">
              <nav class="pagination">
                <a class="pagination-previous">Previous</a>
                <a class="pagination-next">Next</a>
                <ul class="pagination-list">
                  <li>
                    <a class="pagination-link is-current">1</a>
                  </li>
                  <li>
                    <a class="pagination-link">2</a>
                  </li>
                  <li>
                    <a class="pagination-link">3</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      warehouseorders: []
    }
  },
  mounted () {
    console.log('mounted')

    axios
      .get('/api/v1/orders')
      .then(response => {
        console.log(response.data)

        this.warehouseorders = response.data
      })
  }
}
</script>
