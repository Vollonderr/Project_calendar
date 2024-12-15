const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        valve: new Date().getDay(),
        text: []
    }
})