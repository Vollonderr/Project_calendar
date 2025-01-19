const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: () => ({
      events_count: 0,
      update_value: '',
      importance_change: '',
      status_change: '',
      valve_add: false,
      valve_date: false
    }),
    methods:{
      get_events: function(e) {
        return e.slice(0)
      },

      get_importance_value: function(e) {
        if(e === '') return '0'
        return e
      },

      get_status_value: function(e) {
        if(e === '') return '0'
        return e
      },

      get_valve_date: function(e) {
        if(e == 0) return true
        else return false
      }

    }
})

