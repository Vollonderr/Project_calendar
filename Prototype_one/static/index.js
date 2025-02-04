const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: () => ({
      name_select: '',
      note_select: '',
      supervisor_select: '',
      update_value: '',
      importance_change: '',
      status_change: '',
      valve_add: false,
      valve_date: false
    }),
    methods:{
      get_info: function(e) {
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
      },

      get_select: function(e, c) {
        if(c.toLowerCase().search(e.toLowerCase()) != -1) return true
        else return false
      }

    }
})

