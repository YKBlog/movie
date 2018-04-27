layui.use(['flow', 'element'], function () {
    var flow = layui.flow;
    var element = layui.element;
    var douban_id = $('#douban_id').val();
    flow.load({
        elem: '#comment_list' //指定列表容器
        , isAuto: true
        , end: '~~ 我也是有底线的 ~~'
        , done: function (page, next) { //到达临界点（默认滚动触发），触发下一页
            var lis = [];
            //以jQuery的Ajax请求为例，请求下一页数据（注意：page是从2开始返回）
            $.get('/comment_more/' + douban_id + '/' + page, function (res) {
                //假设你的列表返回在data集合中
                layui.each(res.comments, function (index, item) {
                    html = '<div class="layui-col-md12" style="margin: 15px 0;">';
                    html += '<span style="color:#37a">' + item.nickname + '</span>';
                    html += '<span style="padding: 0 20px;">' + item.comment_time + '</span>';
                    html += '评分：<span class="layui-badge">' + item.score + '</span></div>';
                    html += '<div class="layui-col-md12" style="border-bottom: 1px solid #ccc;padding-bottom: 15px;">' + item.content + '</div>';
                    lis.push(html);
                });

                //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
                //pages为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
                next(lis.join(''), page < res.total_page);
            });
        }
    });
});