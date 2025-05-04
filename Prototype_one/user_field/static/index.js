const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: () => ({
      count: 0,
      name_select: '',
      note_select: '',
      supervisor_select: '',
      supervisor_info_select: '',
      date_select1: '',
      date_select2: '',
      importance_change: '',
      status_change: '',
      color_text: '',
      color_BG: '',
      color_BGLOW: '',
      color_lines: '',
      valve_color: true
    }),
    methods:{
      get_info: function(e) {
        return e.slice(0)
      },

      get_select: function(e, c) {
        if(c.toLowerCase().search(e.toLowerCase()) != -1) return true
        else return false
      },

      color_change: function(text, BG, BGLOW, lines) {
        if(this.valve_color == true) {
          this.color_text = text
          this.color_BG = BG
          this.color_BGLOW = BGLOW
          this.color_lines = lines
          this.valve_color = false
        }
        return this.valve_color
      },

      get_select_date: function(e1, e2, c1, c2) {
        const date_search1 = new Date(e1).getTime()
        const date_search2 = new Date(e2).getTime()
        const date_real1 = new Date(c1).getTime()
        const date_real2 = new Date(c2).getTime()


        if(e2 == '') {
          if(date_search1 == date_real1) return true
          else if(date_search1 >= date_real1 && date_search1 <= date_real2) return true
          else return false
        }

        else if(c2 == 0) {
          if(date_search1 <= date_real1 && date_search2 >= date_real1) return true
          else return false
        }

        else {
          if(date_search1 >= date_real1 && date_search1 <= date_real2 || date_search2 >= date_real1 && date_search2 <= date_real2) return true
          if(date_search1 <= date_real1 && date_search2 >= date_real2) return true
          else return false
        }
      }

    }
})

