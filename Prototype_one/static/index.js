const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: () => ({
      event_all: [],
      update_value: '',
      importance_value: '0',
      status_value: '0',
      importance_change: '',
      valve_add: false,
      valve_date: false
    }),
    methods:{
      get_events: function(e) {
        this.event_all = e.slice(0)
        return this.event_all
      },

      get_importance_value: function(e) {
        this.importance_value = e
        return this.importance_value
      },

      get_status_value: function(e) {
        this.status_value = e
        return this.status_value
      },

      get_valve_date: function(e) {
        if(e == 0) return true
        else return false
      }
    }
})

