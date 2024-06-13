const blogsCont = document.querySelector('.blogs');

function createBlogs(blogs) {
	blogsCont.innerHTML = '';
	blogs.forEach((blog) => {
		blogsCont.innerHTML += `<div class="card">
                                    <div class="card-body">
                                        <div>
                                            <h5 class="card-title">${blog.title}</h5>
                                            <p class="card-text">
                                                ${blog.content}
                                            </p>
                                        </div>
                                        <a href="#" class="btn btn-primary">Detail</a>
                                    </div>
                                </div>`;
	});
}

const getBlogs = async () => {
	const response = await fetch('http://127.0.0.1:8000/blog-api/list/');
	const result = await response.json();
	console.log(result);
	createBlogs(result);
};

getBlogs();
