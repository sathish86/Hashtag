var app = angular.module('noteHash', []);
app.controller('noteCtrl', function($scope,$http) {

    var local_host = "http://localhost:8000/"
    var api_notes = "api/v1/note/?format=json"
    var api_hash_tags = "api/v1/hashtag/?format=json"

    var api_note_post = "api/v1/note/page/"

    $scope.note_python = "Python Blog";
    $scope.note_hb = "Heart breakers";
    $scope.note_bbd = "Big billion day";

    $scope.notes_data = function() {
        // call API to fetch notes data
        $http.get(local_host+api_notes)
          .success(function (response) {
                console.log("Notes data Success");
                $scope.notes_list = response.objects;
                console.log($scope.notes_list)
                console.log($scope.notes_list.length)
            });
    }

    $scope.hashtag_data = function() {
        // call API to fetch hashtag data
        $http.get(local_host+api_hash_tags)
          .success(function (response) {
                console.log("HashTags data Success");
                $scope.hash_tags_list = response.objects;
                console.log(response.objects);
                console.log(response.objects[0]);
            });
    }

    $scope.create_note = function(note_desc) {
        // call API to create note data, which internally create data for hashtags
        console.log(note_desc);
        var input_data = {};
        input_data["description"] = note_desc
        
        $http({
            method: 'POST',
            url: local_host+api_note_post,
            data: input_data,
            headers: {'Content-Type': 'application/json'}
        })
        .success(function (response) {
                console.log("POST Success");
                $scope.notes_data();
                $scope.hashtag_data();
            });      
          
    }

    $scope.related_notes = function(hashtag_notes) {
        console.log("related notes");
        $scope.notes_list = hashtag_notes
    }

    $scope.notes_data();
    $scope.hashtag_data();


});